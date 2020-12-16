using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyPath : MonoBehaviour
{
    [SerializeField]
    private GameObject path;
    [SerializeField]
    private float moveSpeed = 2f;
    int waypointIndex = 0;

    void Start()
    {
        this.transform.position = path.transform.GetChild(waypointIndex).transform.position;
    }

    void Update()
    {
        if (waypointIndex < path.transform.childCount)
        {
            var targetPosition = path.transform.GetChild(waypointIndex).transform.position;

            float move = moveSpeed * Time.deltaTime;

            transform.position = Vector2.MoveTowards(transform.position, targetPosition, move);

            if (transform.position == targetPosition)
            {
                waypointIndex++;
            }
        }
        else
        {
            //waypointIndex = 0;
            Destroy(this.gameObject);
        }
    }

    void StartPath()
    {
    }
}
